import logging
import logging.config
import sys
import ddtrace

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger()

ddtrace.config.service = 'Observability-PY'
ddtrace.config.env = 'dev'

with ddtrace.tracer.trace('minha-operacao'):
    try:
        logger.info("Iniciando a aplicação", extra={'user': 'sistema x'})
    except OSError as e:
        logger.error("Ocorreu um erro: %s", e, extra={'user': 'sistema x'})
        sys.exit(1)