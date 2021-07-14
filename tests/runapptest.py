import superset

app = superset.create_app()
app.run("0.0.0.0", debug=True)
