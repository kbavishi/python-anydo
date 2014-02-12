# -*- coding: utf-8 -*-
import auth
from bind import bind_method


class AnyDoAPI(auth.AnyDoSession):
    host = "https://sm-prod.any.do"

    def __init__(self, username, password):
        super(AnyDoAPI, self).__init__(username=username,
                                       password=password)

    """
    Fetches user information
    """
    user_info = bind_method(path="/me",
                            method="GET")

    """
    Fetches tasks (including notes)
    """
    tasks = bind_method(path="/me/tasks",
                        method="GET",
                        accepts_parameters=["responseType",
                                            "includeDeleted",
                                            "includeDone"
                                            ]
                        )

    """
    Fetches categories
    """
    categories = bind_method(path="/me/categories",
                             method="GET",
                             accepts_parameters=["responseType",
                                                 "includeDeleted",
                                                 "includeDone"
                                                 ]
                             )