#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CrossBox():
    """CrossBox is a side project to manage a CrossFit gym.

    It handles users, training sessions calendar, reservations and periodic
    payments with Stripe.

    It's in production since 2 years with expectations of growing.
    """

    @property
    def frontend():
        """It's served with Django Templates and VueJs components."""
        pass

    @property
    def backend():
        """Django"""
        pass

    @property
    def deployment():
        """The deployment is configured by Ansible in EC2 (prev in GCP vm)

        An Nginx in front redirecting to a uwsgi unix socket to communicate
        with the app.
        """
        pass
