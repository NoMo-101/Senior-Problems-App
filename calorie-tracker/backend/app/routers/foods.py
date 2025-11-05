from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase
from pydantic import BaseModel

router = APIRouter()

class FoodEntry(BaseModel):
    food_name: str
    calories: int
    protein: float
    carbs: float
    fat: float
    servings: float
    meal_type: str  # breakfast, lunch, dinner, snack

@router.post("/log")
async def log_food(entry: FoodEntry, user_id: str):
    """Log a food entry for a user"""
    try:
        data = supabase.table("food_entries").insert({
            "user_id": user_id,
            "food_name": entry.food_name,
            "calories": entry.calories,
            "protein": entry.protein,
            "carbs": entry.carbs,
            "fat": entry.fat,
            "servings": entry.servings,
            "meal_type": entry.meal_type
        }).execute()
        
        return {"message": "Food logged successfully!", "data": data.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/daily/{user_id}")
async def get_daily_foods(user_id: str):
    """Get all food entries for a user today"""
    try:
        data = supabase.table("food_entries").select("*").eq("user_id", user_id).execute()
        
        # Calculate total calories
        total_calories = sum(item['calories'] for item in data.data)
        
        return {
            "foods": data.data,
            "total_calories": total_calories
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))