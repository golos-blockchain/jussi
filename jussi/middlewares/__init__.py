# -*- coding: utf-8 -*-


from .jussi import finalize_jussi_response
from .limits import check_limits
from .caching import get_response
from .caching import cache_response
from .update_block_num import update_last_irreversible_block_num


def setup_middlewares(app):
    logger = app.config.logger
    logger.info('setup_middlewares', when='before_server_start')

    # request middleware
    app.request_middleware.append(check_limits)
    app.request_middleware.append(get_response)

    # response middlware
    app.response_middleware.append(finalize_jussi_response)
    app.response_middleware.append(update_last_irreversible_block_num)
    app.response_middleware.append(cache_response)

    logger.info('configured request middlewares', middlewares=app.request_middleware)
    logger.info('configured response middlewares', middlewares=app.response_middleware)
    return app
