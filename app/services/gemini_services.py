import os
import google.generativeai as genai
import json
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_smart_workout(self, prompt: str, user_type: str, mood: str):
        persona = "Hero RPG" if user_type == "teen" else "Pro Coach"
        
        # Tambahkan instruksi paksaan agar AI hanya memberi JSON
        system_instruction = f"""
        Tugas: Buat rencana latihan untuk {prompt}.
        Persona: {persona}. Kondisi: {mood}.
        
        PENTING: Hanya berikan output dalam format JSON murni. 
        Jangan berikan teks pembuka atau penutup apapun.
        {{
            "display_text": "rencana detail di sini",
            "audio_script": "pesan suara singkat"
        }}
        """

        try:
            response = self.model.generate_content(system_instruction)
            raw_text = response.text.strip()
            
            # DEBUG: Print hasil asli AI ke terminal kita
            print(f"DEBUG - Raw AI Response: {raw_text}")

            # Pembersihan Markdown yang lebih kuat
            if "```json" in raw_text:
                raw_text = raw_text.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_text:
                raw_text = raw_text.split("```")[1].split("```")[0].strip()

            return json.loads(raw_text)
            
        except Exception as e:
            # Ini akan muncul di terminal Python Anda
            print(f"ERROR DETAIL: {str(e)}") 
            return {
                "display_text": f"Gagal memproses data AI. Error: {str(e)}",
                "audio_script": "Terjadi kesalahan."
            }

gemini_service = GeminiService()