# import sys
# from PyQt5.QtWidgets import QApplication
# from harvesters_gui.frontend.pyqt5 import Harvester
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     h = Harvester()
#     h.show()
#     sys.exit(app.exec_())

from harvesters.core import Harvester
import sys
import traceback
import cv2

#dsx
# def unique(list1):
#     # insert the list to the set
#     list_set = set(list1)
#     # convert the set to the list
#     unique_list = (list(list_set))
#     for x in unique_list:
#         print(x)
#     return x
#dsx
def main():
    h = Harvester()
    h.add_cti_file('C:/Program Files/JAI/SDK/bin/JaiGevTL.cti')
    # JaiUSB3vTL  JaiGevTL
    print(h.cti_files)
    h.update_device_info_list()
    print("file",h.device_info_list)
    print("dty",list(dict.fromkeys(h.device_info_list)))



    # x = unique(h.device_info_list)
    # print("pp",x)
    print("devices end")
    ia = h.create_image_acquirer(0)
    print("dsssx",ia.device)
    print("infor",ia.device.node_map.device_info)
    # ia.device.node_map.Test
    # ia.device.node_mapdsx key.PixelFormat.value = 'RGB12'
    # ia.device.node_map.RGB12Packed.value = 'RGB12'
    # ia.device.node_map.has_node()
    # ia.device.node_map.TestPattern = 'HorizontalColorBar'
    # ia.acquirer.remote_device.node_map
    print(ia.is_acquiring())

    try:
        print("acqui")
        ia.start_image_acquisition()
        print("acquired",ia.is_acquiring())
        print("acqui 2",ia.fetch_buffer())
        i = 0
        done = False
        while not done:
            with ia.fetch_buffer() as buffer:
                print("checkr 1")
                img = buffer.payload.components[0].data
                img = img.reshape(buffer.payload.components[0].height, buffer.payload.components[0].width)
                # img_copy = img.copy()
                img_copy = cv2.cvtColor(img, cv2.COLOR_BayerRG2RGB)
                cv2.namedWindow("window", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
                cv2.imshow("window", img_copy)
                fps = ia.statistics.fps
                print("FPS: ", fps)
                if cv2.waitKey(10) == ord('q'):
                    done = True
                    print('break')
                i = i + 1
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
    finally:
        ia.stop_image_acquisition()
        ia.destroy()
        cv2.destroyAllWindows()
        print('fin')
        h.reset()

if __name__ == "__main__":
    main()
# [(id_='MAC->00-0C-DF-04-94-35::JAI Ltd., Japan::AD-080GE_#0', vendor='JAI Ltd., Japan', model='AD-080GE_#0', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#  (id_='MAC->00-0C-DF-04-A4-35::JAI Ltd., Japan::AD-080GE_#1', vendor='JAI Ltd., Japan', model='AD-080GE_#1', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#  (id_='MAC->00-0C-DF-04-94-35::JAI Ltd., Japan::AD-080GE_#0', vendor='JAI Ltd., Japan', model='AD-080GE_#0', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#  (id_='MAC->00-0C-DF-04-A4-35::JAI Ltd., Japan::AD-080GE_#1', vendor='JAI Ltd., Japan', model='AD-080GE_#1', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None)]


# pp (id_='MAC->00-0C-DF-04-94-35::JAI Ltd., Japan::AD-080GE_#0', vendor='JAI Ltd., Japan', model='AD-080GE_#0', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None)
# file [(id_='MAC->00-0C-DF-04-94-35::JAI Ltd., Japan::AD-080GE_#0', vendor='JAI Ltd., Japan', model='AD-080GE_#0', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#       (id_='MAC->00-0C-DF-04-A4-35::JAI Ltd., Japan::AD-080GE_#1', vendor='JAI Ltd., Japan', model='AD-080GE_#1', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#       (id_='MAC->00-0C-DF-04-94-35::JAI Ltd., Japan::AD-080GE_#0', vendor='JAI Ltd., Japan', model='AD-080GE_#0', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None),
#       (id_='MAC->00-0C-DF-04-A4-35::JAI Ltd., Japan::AD-080GE_#1', vendor='JAI Ltd., Japan', model='AD-080GE_#1', tl_type='GEV', user_defined_name=None, serial_number='X801289', version=None)]
