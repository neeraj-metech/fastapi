Run This project please follow below instractions
==================================================
1. crate a virtural enverment on any directory
    python -m venv fast-env
2. activate the enverment
    .\fast-env\Scripts\activate
3. intall fastapi package
    pip install -r requirment.txt
    python.exe -m pip install --upgrade pip
4. run this
    fastapi dev blog/main.py




Fast API Basic instractions
===========================
1. crate a virtural enverment on any directory
    python -m venv fast-env
2. activate the enverment
    .\fast-env\Scripts\activate
3. intall fastapi package
    pip install "fastapi[standard]"
4. Now create a main.py file
5. Now run it
    fastapi dev main.py || fastapi dev blog/main.py
            OR  
    uvicorn main:app --reload || uvicorn blog.main:app --reload