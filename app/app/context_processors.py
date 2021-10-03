import app.settings

def global_variables_processor(request):
    return {'APP_TITLE': app.settings.APP_TITLE}