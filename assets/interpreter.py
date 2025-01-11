from flet import ControlEvent
import sys
import io

def interpreter(input: str) -> str:
    """Fonction qui interprete et qui renvoit le resultat"""
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    try:
        exec(input)
        result = sys.stdout.getvalue()
        error = sys.stderr.getvalue()
        if error:
            return f"Erreur: \n{error}"
        else:
            return result if result else "Code excecute avec succes"
    except Exception as e: 
        return f"Exception: {e}"
    
if __name__ == "__main__":
    code = input('> ')
    print(interpreter(code))
    input()