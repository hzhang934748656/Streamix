def Singleton(klass):
    if not klass._instance:
        klass._instance = klass()
    return klass._instance


class Data_bridge:
    _instance = None

    def __init__(self):
        self.methode_chosen_by_radio_butten = ''
        self.start_process_manager = False
        self.save_data_in_video_format = False
        self.save_data_in_image_format = True
        self.selected_video_file_path = ''
        self.selected_background_file_path = ''
        pass
