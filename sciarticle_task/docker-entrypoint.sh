if [ "$DEBUG" = "True" ]; then
    echo "debug mode"
    uvicorn application.api.main:app --reload
else
    echo "release mode"
    uvicorn application.api.main:app
fi