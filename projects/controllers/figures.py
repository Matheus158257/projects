# -*- coding: utf-8 -*-
"""Figures controller."""

import platiagro


def list_figures(experiment_id, operator_id):
    """Lists all figures from object storage as data URI scheme.

    Args:
        experiment_id (str): the experiment uuid.
        operator_id (str): the operator uuid.

    Returns:
        A list of data URIs.
    """
    return platiagro.list_figures(experiment_id=experiment_id,
                                  operator_id=operator_id)
