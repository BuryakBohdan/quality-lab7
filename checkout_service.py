from dataclasses import dataclass

@dataclass(frozen=True)
class MoneyContext:
    base_amount: float
    currency: str
    tax_rate: float

    def with_discount(self, factor: float) -> float:
        return self.base_amount * factor

    def apply_tax(self, amount: float) -> float:
        return round(amount * (1 + self.tax_rate), 2)

@dataclass(frozen=True)
class DiscountPolicy:
    discount_code: str
    is_vip: bool

    def get_multiplier(self) -> float:
        if self.is_vip:
            return 0.85
        return 0.90 if self.discount_code == "PROMO10" else 1.0

def calculate_checkout_total(money: MoneyContext, policy: DiscountPolicy, user_id: int, logger) -> float:
    # Жодної мутабельної змінної (M = 0), жодного if/else у методі (C = 0)
    discounted = money.with_discount(policy.get_multiplier())
    final_total = money.apply_tax(discounted)
    logger.info(f"User {user_id}: total={final_total} {money.currency}")
    return final_total
# iteration 1
# iteration 2
# iteration 3
# iteration 4
# iteration 5
# iteration 6
# iteration 7
# iteration 8
# iteration 9
