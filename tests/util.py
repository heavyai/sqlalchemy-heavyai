from werkzeug.routing import MethodNotAllowed, NotFound, RequestRedirect


def get_view_function(url, app, method="GET"):
    """Match a url and return the view and arguments
    it will be called with, or None if there is no view.
    """

    adapter = app.url_map.bind("localhost")
    import pdb

    pdb.set_trace()

    try:
        match = adapter.match(url, method=method)
    except RequestRedirect as e:
        # recursively match redirects
        return get_view_function(e.new_url, method)
    except (MethodNotAllowed, NotFound):
        # no match
        return None

    try:
        # return the view function and arguments
        return app.view_functions[match[0]], match[1]
    except KeyError:
        # no view is associated with the endpoint
        return None


if __name__ == "__main__":
    import superset

    app = superset.create_app()

    """
    (<bound method ModelRestApi.get_list of
     <superset.datasets.api.DatasetRestApi object at 0x7f193c1ecc50>>, {})
    """
    result = get_view_function("/api/v1/dataset/", app=app)
    print(result)
