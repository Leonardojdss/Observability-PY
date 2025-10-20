import logging
import sys
import ddtrace

# Configurar logging para arquivo e console
logging.basicConfig(
    level=logging.DEBUG,
    filename='/tmp/observability-py.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Console
        logging.FileHandler('/tmp/observability-py.log')  # Arquivo para Datadog
    ]
)
logger = logging.getLogger(__name__)

ddtrace.config.service = 'Observability-PY'
ddtrace.config.env = 'dev'

with ddtrace.tracer.trace('minha-operacao'):
    logger.info('usuario criado', extra={'user': 'Leonardo'})
    
    #logger.error('Algo deu errado')