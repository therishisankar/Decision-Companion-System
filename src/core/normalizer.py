class Normalizer:
    @staticmethod
    def scale(value: float, min_val: float, max_val: float, is_cost: bool) -> float:
        """
        Normalizes a value to 0.0 - 1.0 range.
        - Benefit (is_cost=False): (val - min) / (max - min)
        - Cost (is_cost=True): (max - val) / (max - min)
        """
        if max_val == min_val:
            return 1.0  # If no variance, all options get full score for this criterion
        
        if is_cost:
            normalized = (max_val - value) / (max_val - min_val)
        else:
            normalized = (value - min_val) / (max_val - min_val)
            
        return max(0.0, min(1.0, normalized))
