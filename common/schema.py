import minipb

@minipb.process_message_fields
class StateMessage(minipb.Message):
    t_seconds = minipb.Field(1, minipb.TYPE_UINT) # in seconds
    temp_c = minipb.Field(2, minipb.TYPE_FLOAT)
    slope = minipb.Field(3, minipb.TYPE_FLOAT)
