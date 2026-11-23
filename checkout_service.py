def calculate_checkout_total(base_amount: float, currency: str, tax_rate: float, discount_code: str, is_vip: bool, user_id: int, logger):
    total = base_amount
    status = "PENDING"
    
    if is_vip:
        total = total * 0.85
        status = "VIP_APPLIED"
    elif discount_code == "PROMO10":
        total = total - (total * 0.10)
        status = "PROMO_APPLIED"
        
    # БАГ МУТАЦІЇ: розробник випадково перезаписав 'total' замість додавання податку
    total = total * tax_rate  
    
    logger.info(f"User {user_id}: total={total} {currency}, status={status}")
    return round(total, 2)
