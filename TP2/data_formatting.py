class DataFormatting:
    
    @staticmethod
    def format_data(cleaned_data: dict) -> dict:
        
        cleaned_data["bmi"] = cleaned_data["weight"] / (cleaned_data["height"] ** 2)
        
        return cleaned_data