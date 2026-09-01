"""
Investment Portfolio Service
"""
import uuid
import random
from datetime import datetime
from typing import List, Dict, Any
from storage.file_storage import FileStorageEngine
from storage.json_repository import JsonRepository

class InvestmentService:
    def __init__(self, storage: FileStorageEngine):
        self.repo = JsonRepository(storage, "holdings.json", id_field="id")
        self._ensure_sample_holdings()

    def _ensure_sample_holdings(self):
        holdings = self.repo.get_all()
        if not holdings:
            sample_holdings = [
                ("user_customer_01", "VOO", "Vanguard S&P 500 ETF", "ETF", 50.0, 410.20, 485.50)
            ]
            for u_id, sym, name, asset_cls, qty, buy_px, curr_px in sample_holdings:
                h = {
                    "id": f"hld_{uuid.uuid4().hex[:12]}",
                    "user_id": u_id,
                    "symbol": sym,
                    "name": name,
                    "asset_class": asset_cls,
                    "quantity": float(qty),
                    "purchase_price": float(buy_px),
                    "current_price": float(curr_px),
                    "last_updated": datetime.utcnow().isoformat()
                }
                self.repo.add(h)

    def get_user_portfolio(self, user_id: str) -> Dict[str, Any]:
        holdings = self.repo.find(lambda h: h.get("user_id") == user_id)
        total_cost = 0.0
        total_value = 0.0
        asset_allocation = {}
        
        for h in holdings:
            qty = h.get("quantity", 0.0)
            buy_px = h.get("purchase_price", 0.0)
            curr_px = h.get("current_price", 0.0)
            cost_basis = round(qty * buy_px, 2)
            market_val = round(qty * curr_px, 2)
            gain_loss = round(market_val - cost_basis, 2)
            gain_loss_pct = round((gain_loss / cost_basis) * 100, 2) if cost_basis > 0 else 0.0
            
            h["cost_basis"] = cost_basis
            h["market_value"] = market_val
            h["gain_loss"] = gain_loss
            h["gain_loss_pct"] = gain_loss_pct
            
            total_cost += cost_basis
            total_value += market_val
            cls = h.get("asset_class", "OTHER")
            asset_allocation[cls] = round(asset_allocation.get(cls, 0.0) + market_val, 2)
            
        total_gain_loss = round(total_value - total_cost, 2)
        total_gain_pct = round((total_gain_loss / total_cost) * 100, 2) if total_cost > 0 else 0.0
        
        return {
            "holdings": holdings,
            "total_cost": round(total_cost, 2),
            "total_value": round(total_value, 2),
            "total_gain_loss": total_gain_loss,
            "total_gain_pct": total_gain_pct,
            "asset_allocation": asset_allocation,
            "diversification_score": 80
        }

    def get_portfolio_summary(self, user_id: str) -> Dict[str, Any]:
        return self.get_user_portfolio(user_id)

    def add_holding(self, user_id: str, symbol: str, name: str, asset_class: str, quantity: float, purchase_price: float, current_price: float) -> Dict[str, Any]:
        h = {
            "id": f"hld_{uuid.uuid4().hex[:12]}",
            "user_id": user_id,
            "symbol": symbol.upper(),
            "name": name,
            "asset_class": asset_class.upper(),
            "quantity": float(quantity),
            "purchase_price": float(purchase_price),
            "current_price": float(current_price),
            "last_updated": datetime.utcnow().isoformat()
        }
        self.repo.add(h)
        return h

    def add_investment(self, user_id: str, asset_name: str, asset_category: str, amount: float, buy_price: float = 100.0) -> Dict[str, Any]:
        qty = amount / buy_price if buy_price > 0 else 1.0
        return self.add_holding(user_id, asset_name[:4].upper(), asset_name, asset_category, qty, buy_price, buy_price)
