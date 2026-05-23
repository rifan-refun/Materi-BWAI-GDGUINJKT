from fastapi import APIRouter, HTTPException
from app.schemas.workout import WorkoutRequest, WorkoutResponse
from app.services.gemini_services import gemini_service

router = APIRouter()

@router.post("/generate", response_model=WorkoutResponse)
async def create_workout(payload: WorkoutRequest):
    try:
        ai_data = await gemini_service.generate_smart_workout(
            payload.prompt, payload.user_type, payload.mood
        )
        return WorkoutResponse(
            ai_content=ai_data['display_text'],
            is_rpg_mode=(payload.user_type == "teen"),
            audio_script=ai_data['audio_script']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
