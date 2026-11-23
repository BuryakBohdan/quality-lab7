import logging
from checkout_service import calculate_checkout_total, MoneyContext, DiscountPolicy

def test_checkout_immutable_pass():
    logger = logging.getLogger("test")
    money = MoneyContext(base_amount=100.0, currency="USD", tax_rate=0.20)
    policy = DiscountPolicy(discount_code="", is_vip=True)
    
    result = calculate_checkout_total(money, policy, 1, logger)
    assert result == 102.0
