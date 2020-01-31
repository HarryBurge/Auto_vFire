from PIL import Image
import random

Imgs_to_crop = ['None_Title',
                'CallTempRed',
                'AdminGrey',
                'None_Top_Black',
                'CMDBItemsGrey',
                'AdminRed',
                'None_Version',
                'None_White',
                'None_Top_BR',
                'CMDBItemsRed',
                'Box_Select_Call',
                'RedBannerNone',
                'RequestBox',
                'None_Top_Buttons',
                'DesignerGrey',
                'Box_Select_Request',
                'SearchGrey',
                'SearchRed',
                'None_Top',
                'DesignerRed',
                'Box_Select_Task',
                'SysAdminGrey',
                'SysAdminRed',
                'TaskBox',
                'MenuButton',
                'CallBox',
                'WorkflowTempGrey',
                'WorkflowTempRed',
                'None_Banner',
                'CallTempGrey']
for i in Imgs_to_crop:

    im = Image.open(i+'.JPG')
    truewidth, trueheight = im.size

    for j in range(0, 21):
        ranleft = random.randint(0, truewidth//4)
        rantop = random.randint(0, trueheight//4)

        ranwidth = random.randint(3*truewidth//4, truewidth)
        ranheight = random.randint(3*trueheight//4, trueheight)

        left = ranleft
        top = rantop

        height = ranheight - rantop
        width = ranwidth - ranleft

        print('Training_Data_/'+i+'_'+str(j)+'.JPG')
        im1 = im.crop((left, top, left+width, top+height))
        im1 = im1.save('Training_Data_/'+i+'_'+str(j)+'.JPG')
