if [ "$APP_DEBUG" = "True" ]; then
    echo "debug mode"
    uvicorn application.api.main:app --reload --host 0.0.0.0 --port 8000
else
    echo "release mode"
    uvicorn application.api.main:app --host 0.0.0.0 --port 8000
fi