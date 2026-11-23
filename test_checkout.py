import logging
from checkout_service import calculate_checkout_total

def test_checkout_mutation_bug():
    logger = logging.getLogger("test")
    # Очікуємо: 100 * 0.85 (VIP) + 20% податок = 102.0
    # Через баг мутації отримаємо 17.0 (касовий розрив)
    result = calculate_checkout_total(100.0, "USD", 0.20, "", True, 1, logger)
    assert result == 102.0, f"CRITICAL MUTATION BUG: expected 102.0, got {result}"
