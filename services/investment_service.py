"""
Investment Portfolio & Market Performance Simulator
Manages stocks, ETFs, mutual funds, bonds, gold holdings, diversification scoring, and simulated price ticks.
"""

import uuid
import random
from datetime import datetime
from typing import List, Dict, Any, Optional
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
                ("user_customer_01", "VOO", "Vanguard S&P 500 ETF", "ETF", 50.0, 410.20, 485.50),
                ("user_customer_01", "AAPL", "Apple Inc Common Stock", "STOCKS", 35.0, 165.50, 224.30),
                ("user_customer_01", "MSFT", "Microsoft Corp Common Stock", "STOCKS", 25.0, 310.00, 448.90),
                ("user_customer_01", "BND", "Vanguard Total Bond Market ETF", "BONDS", 100.0, 72.50, 74.10),
                ("user_customer_01", "GLD", "SPDR Gold Shares ETF", "GOLD", 20.0, 185.00, 232.40)
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
        
        # Calculate diversification score (0-100) based on asset class spread
        num_classes = len(asset_allocation)
        diversification_score = min(num_classes * 20, 100)
        
        return {
            "holdings": holdings,
            "total_cost": round(total_cost, 2),
            "total_value": round(total_value, 2),
            "total_gain_loss": total_gain_loss,
            "total_gain_pct": total_gain_pct,
            "asset_allocation": asset_allocation,
            "diversification_score": diversification_score
        }

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

    def simulate_market_tick(self, user_id: str) -> List[Dict[str, Any]]:
        holdings = self.repo.find(lambda h: h.get("user_id") == user_id)
        for h in holdings:
            change_pct = random.uniform(-0.025, 0.035)
            curr_px = h.get("current_price", 100.0)
            new_px = max(round(curr_px * (1 + change_pct), 2), 1.0)
            self.repo.update(h["id"], {"current_price": new_px, "last_updated": datetime.utcnow().isoformat()})
        return holdings
