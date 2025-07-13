tortoise-plus BlackSheep example
============================

We have a lightweight integration util ``tortoise.contrib.blacksheep`` which has a single function ``register_tortoise`` which sets up tortoise-plus on startup and cleans up on teardown.

Usage
-----

.. code-block:: sh

    uvicorn server:app --reload
