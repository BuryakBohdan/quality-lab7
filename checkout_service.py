def calculate_checkout_total(base_amount: float, currency: str, tax_rate: float, discount_code: str, is_vip: bool, user_id: int, logger):
    # Лінійний метод (CC = 3), але багато мутабельних змінних
    total = base_amount
    status = "PENDING"
    
    if is_vip:
        total = total * 0.85
        status = "VIP_APPLIED"
    elif discount_code == "PROMO10":
        total = total - (total * 0.10)
        status = "PROMO_APPLIED"
        
    tax_amount = total * tax_rate
    total = total + tax_amount
    
    logger.info(f"User {user_id}: total={total} {currency}, status={status}")
    return round(total, 2)
