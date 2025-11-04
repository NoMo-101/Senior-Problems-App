from fastapi import FastAPI
from app.supabase_client import supabase

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Calorie Tracker API"}

@app.get("/test-supabase")
def test_supabase():
    try:
        # Try to query food_entries table
        result = supabase.table("food_entries").select("*").limit(5).execute()
        return {
            "status": "connected", 
            "data": result.data,
            "count": len(result.data)
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}