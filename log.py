import os

from lithoxyl import Logger, SensibleSink, Formatter, StreamEmitter
from lithoxyl.emitters import FileEmitter
from lithoxyl.filters import ThresholdFilter

class FixedFileEmitter(FileEmitter):
    def __init__(self, filepath, encoding=None, **kwargs):
        self.encoding = encoding
        super(FixedFileEmitter, self).__init__(filepath, encoding, **kwargs)

LOGFILE = 'lithoxyl.log'  # TODO: where?

tlog = Logger('toplog')

file_fmt = Formatter('{status_char}{end_local_iso8601_noms_notz} - {duration_secs}s - {record_name} - {message}')
file_emt = FixedFileEmitter(LOGFILE)
file_filter = ThresholdFilter(success='critical',
                              failure='info',
                              exception='debug')
file_sink = SensibleSink(formatter=file_fmt,
                         emitter=file_emt,
                         filters=[file_filter])
tlog.add_sink(file_sink)


def set_debug(enable=True):
    if not enable:
        raise NotImplementedError()
    dbg_fmtr = file_fmt
    dbg_emtr = StreamEmitter('stderr')
    
    dbg_sink = SensibleSink(formatter=dbg_fmtr,
                            emitter=dbg_emtr)
    tlog.add_sink(dbg_sink)
    
