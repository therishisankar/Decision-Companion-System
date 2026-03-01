class Normalizer:
    # This function turns a number into a score between 0 and 1.
    # Higher is better for things like 'Reliability'
    # Lower is better for things like 'Cost'
    @staticmethod
    def scale(value: float, min_val: float, max_val: float, is_cost: bool) -> float:
        if max_val == min_val:
            return 1.0  # If no variance, all options get full score for this criterion
        
        if is_cost:
            normalized = (max_val - value) / (max_val - min_val)
        else:
            normalized = (value - min_val) / (max_val - min_val)
            
        return max(0.0, min(1.0, normalized))
