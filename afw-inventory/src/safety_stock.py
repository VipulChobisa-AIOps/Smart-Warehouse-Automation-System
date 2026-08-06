import math
import scipy.stats as stats

def calculate_safety_stock(avg_demand, std_dev_demand, avg_lead_time, std_dev_lead_time, service_level=0.95):
    """
    Calculates safety stock under variable demand and variable lead time.
    Uses the statistical Z-score for the targeted service level.
    """
    # Find Z-score for desired service level (e.g. 0.95 -> 1.645)
    z_score = stats.norm.ppf(service_level)
    
    # Combined standard deviation of demand during lead time
    # Formula: sqrt(LT * var_demand + Demand^2 * var_lead_time)
    lead_time_variance = avg_lead_time * (std_dev_demand ** 2) + (avg_demand ** 2) * (std_dev_lead_time ** 2)
    combined_std_dev = math.sqrt(lead_time_variance)
    
    safety_stock = z_score * combined_std_dev
    return math.ceil(safety_stock)

def calculate_reorder_point(avg_demand, avg_lead_time, safety_stock):
    """
    ROP = Lead Time Demand + Safety Stock
    """
    lead_time_demand = avg_demand * avg_lead_time
    return math.ceil(lead_time_demand + safety_stock)

if __name__ == '__main__':
    # Sample SKU: AFW Fortune Soya Oil 1L
    avg_d = 1200 # average units sold per day
    std_d = 180  # standard deviation of daily demand
    avg_lt = 5   # average delivery lead time (days)
    std_lt = 1.2 # standard deviation of lead time (days)
    
    ss = calculate_safety_stock(avg_d, std_d, avg_lt, std_lt, 0.95)
    rop = calculate_reorder_point(avg_d, avg_lt, ss)
    
    print(f"--- Inventory Planning: SKU #Soya1L ---")
    print(f"Safety Stock Required: {ss} units")
    print(f"Reorder Point (ROP): {rop} units")
