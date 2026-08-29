"""
Time Value of Money (TVM) Financial Mathematics Engine
Provides Present Value (PV), Future Value (FV), Payment (PMT), Number of Periods (NPER), Rate, CAGR, IRR, and NPV.
"""

import math
from typing import List, Optional

class TVMEngine:
    @staticmethod
    def future_value(rate: float, nper: int, pmt: float, pv: float = 0.0, end_of_period: bool = True) -> float:
        """Calculates Future Value (FV) of an investment or loan."""
        if rate == 0:
            return -(pv + pmt * nper)
        factor = (1 + rate) ** nper
        if end_of_period:
            return -(pv * factor + pmt * ((factor - 1) / rate))
        else:
            return -(pv * factor + pmt * (1 + rate) * ((factor - 1) / rate))

    @staticmethod
    def present_value(rate: float, nper: int, pmt: float, fv: float = 0.0, end_of_period: bool = True) -> float:
        """Calculates Present Value (PV) of cash flows."""
        if rate == 0:
            return -(fv + pmt * nper)
        factor = (1 + rate) ** nper
        if end_of_period:
            return -(fv / factor + pmt * ((1 - (1 / factor)) / rate))
        else:
            return -(fv / factor + pmt * (1 + rate) * ((1 - (1 / factor)) / rate))

    @staticmethod
    def pmt(rate: float, nper: int, pv: float, fv: float = 0.0, end_of_period: bool = True) -> float:
        """Calculates periodic payment (PMT) for a loan or annuity."""
        if rate == 0:
            return -(pv + fv) / nper
        factor = (1 + rate) ** nper
        if end_of_period:
            return -(pv * factor + fv) * rate / (factor - 1)
        else:
            return -(pv * factor + fv) * rate / ((factor - 1) * (1 + rate))

    @staticmethod
    def cagr(beginning_value: float, ending_value: float, periods: float) -> float:
        """Calculates Compound Annual Growth Rate (CAGR)."""
        if beginning_value <= 0 or periods <= 0:
            return 0.0
        return (ending_value / beginning_value) ** (1 / periods) - 1.0

    @staticmethod
    def npv(rate: float, cashflows: List[float]) -> float:
        """Calculates Net Present Value (NPV) for a series of periodic cash flows."""
        total = 0.0
        for i, cf in enumerate(cashflows):
            total += cf / ((1 + rate) ** i)
        return total

    @staticmethod
    def irr(cashflows: List[float], guess: float = 0.1, max_iter: int = 100, tol: float = 1e-6) -> Optional[float]:
        """Calculates Internal Rate of Return (IRR) using Newton-Raphson method."""
        rate = guess
        for _ in range(max_iter):
            npv_val = 0.0
            d_npv = 0.0
            for i, cf in enumerate(cashflows):
                npv_val += cf / ((1 + rate) ** i)
                if i > 0:
                    d_npv -= i * cf / ((1 + rate) ** (i + 1))
            if abs(npv_val) < tol:
                return rate
            if abs(d_npv) < 1e-12:
                return None
            rate -= npv_val / d_npv
        return rate if abs(npv_val) < tol else None
