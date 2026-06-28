import os
from functools import lru_cache

import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument, GoogleAPICallError
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()


@lru_cache(maxsize=1)
def get_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="GEMINI_API_KEY is not configured. Set a valid Gemini API key in your environment."
        )

    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

def improve_text(text: str):

    prompt = f"""
        You are an Amharic language assistant.

        Correct grammatical errors and improve the sentence.

        Return only the corrected Amharic text.

        Text:
        {text}
        """

    try:
        response = get_model().generate_content(prompt)
    except InvalidArgument as exc:
        raise HTTPException(
            status_code=503,
            detail="Gemini rejected the API key. Check that GEMINI_API_KEY is a valid key for generativelanguage.googleapis.com."
        ) from exc
    except GoogleAPICallError as exc:
        raise HTTPException(
            status_code=503,
            detail="Gemini request failed. Verify your API key, network access, and model availability."
        ) from exc

    return response.text.strip()