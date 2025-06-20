"""
Wrapper-Starter für PyInstaller-Builds.
Er startet deine Streamlit-App genauso, als würdest du `streamlit run app.py`
in der Shell eintippen – nur eben aus einer EXE heraus.
"""
import os, sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(base_dir)                         # sicheres CWD
    sys.argv = [
        "streamlit", "run", "gui.py",
        "--server.port=8501",
        "--global.developmentMode=false",
        "--logger.level=info",
    ]
    sys.exit(stcli.main())
