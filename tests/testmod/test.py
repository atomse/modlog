import modlog



logger = modlog.getLogger(__name__)


for level in ['debug', 'info', 'warn', 'error', 'critical']:
    getattr(logger, level)(level)
