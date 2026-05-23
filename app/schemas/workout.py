from pydantic import BaseModel, Field
from typing import List, Optional

class ExerciseDetail(BaseModel):
    name: str
    sets: int
    reps: int
    notes: Optional[str] = None

class WorkoutRequest(BaseModel):
    prompt: str = Field(..., example="15 menit latihan dada tanpa alat")
    user_type: str = Field(default="adult", example="teen")
    mood: str = Field(default="normal", example="capek tapi semangat")

class WorkoutResponse(BaseModel):
    ai_content: str
    is_rpg_mode: bool
    audio_script: str