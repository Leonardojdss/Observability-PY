import logging
import json
from datetime import datetime


class CustomJsonFormatter(logging.Formatter):
    """Formatter personalizado para logs em JSON com formato específico"""
    
    def format(self, record):
        # Cria o dicionário base do log
        log_entry = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "service": getattr(record, 'service', 'unknown'),
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Adiciona campos extras se existirem
        if hasattr(record, 'user'):
            log_entry["user"] = record.user
            
        if hasattr(record, 'request_id'):
            log_entry["request_id"] = record.request_id
            
        if hasattr(record, 'trace_id'):
            log_entry["trace_id"] = record.trace_id
            
        # Adiciona informações de exceção se houver
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_entry, ensure_ascii=False)


class CustomTextFormatter(logging.Formatter):
    """Formatter personalizado para logs em texto com cores"""
    
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset
    }
    
    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        reset = self.COLORS['RESET']
        
        # Formato personalizado
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        user = getattr(record, 'user', 'system')
        
        formatted = f"{timestamp} | {color}{record.levelname:<8}{reset} | {user:<12} | {record.getMessage()}"
        
        if record.exc_info:
            formatted += f"\n{self.formatException(record.exc_info)}"
            
        return formatted