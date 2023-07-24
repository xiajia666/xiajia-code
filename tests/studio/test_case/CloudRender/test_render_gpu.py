import os,sys
import yaml
sys.path.append('../../../../all')
import allure
from common.studio_auto import Style3DAuto
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud
from common.logs import Log
#云渲染查看
import pytest
# @pytest.mark.skip
@allure.feature('本地渲染GPU和老版本对比')
@allure.severity(allure.severity_level.BLOCKER)
class TestRenderGpu:

    def setup_method(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始前准备，启动软件")
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info("测试结束")
        self.style.close_style3D()
        self.cloud.delete_cloudrender()
        self.cloud.delete_cloud_sproj("cloud")

    @allure.story('消光gpu和老版本对比')
    def test_render_matte(self):
        self.cloud.delete_local_render('matte', 'matte_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'matte.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("matte", "matte_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "matte" + '\\' + "matte_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "matte" + '\\' + "matte_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "消光材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("matte" ,difference))
        assert difference < 100

    @allure.story('丝绸gpu和老版本对比')
    def test_cloud_render_silk(self):
        self.cloud.delete_local_render('silk', 'silk_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'silk.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("silk", "silk_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "silk" + '\\' + "silk_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "silk" + '\\' + "silk_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "丝绸材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("silk" ,difference))
        assert difference < 100

    @allure.story('反光gpu和老版本对比')
    def test_cloud_render_shiny(self):
        self.cloud.delete_local_render('shiny', 'shiny_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'shiny.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("shiny", "shiny_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "shiny" + '\\' + "shiny_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "shiny" + '\\' + "shiny_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "反光材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("shiny" ,difference))
        assert difference < 100

    @allure.story('绒gpu和老版本对比')
    def test_cloud_render_velvet(self):
        self.cloud.delete_local_render('velvet', 'velvet_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'velvet.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("velvet", "velvet_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "velvet" + '\\' + "velvet_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "velvet" + '\\' + "velvet_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "绒材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("velvet" ,difference))
        assert difference < 100

    @allure.story('皮革gpu和老版本对比')
    def test_cloud_render_leather(self):
        self.cloud.delete_local_render('leather', 'leather_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'leather.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("leather", "leather_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "leather" + '\\' + "leather_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "leather" + '\\' + "leather_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "皮革材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("leather" ,difference))
        assert difference < 100

    @allure.story('金属gpu和老版本对比')
    def test_cloud_render_metal(self):
        self.cloud.delete_local_render('metal', 'metal_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'metal.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("metal", "metal_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "metal" + '\\' + "metal_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "metal" + '\\' + "metal_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "金属材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("metal" ,difference))
        assert difference < 100

    @allure.story('塑料gpu和老版本对比')
    def test_cloud_render_plastic(self):
        self.cloud.delete_local_render('plastic', 'plastic_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'plastic.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("plastic", "plastic_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "plastic" + '\\' + "plastic_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "plastic" + '\\' + "plastic_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "塑料材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("plastic" ,difference))
        assert difference < 100

    @allure.story('镭射gpu和老版本对比')
    def test_cloud_render_laser(self):
        self.cloud.delete_local_render('laser', 'laser_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'laser.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("laser", "laser_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "laser" + '\\' + "laser_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "laser" + '\\' + "laser_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "镭射材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("laser" ,difference))
        assert difference < 100

    # @pytest.mark.skip
    @allure.story('毛皮gpu和老版本对比')
    def test_cloud_render_fur(self):
        self.cloud.delete_local_render('fur', 'fur_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'fur.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("fur", "fur_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "fur" + '\\' + "fur_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "fur" + '\\' + "fur_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "毛皮材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("fur" ,difference))
        assert difference < 100

    @allure.story('自发光gpu和老版本对比')
    def test_cloud_render_light(self):
        self.cloud.delete_local_render('light', 'light_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'light.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("light", "light_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "light" + '\\' + "light_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "light" + '\\' + "light_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "自发光材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("light" ,difference))
        assert difference < 100

    @allure.story('宝石gpu和老版本对比')
    def test_cloud_render_gem(self):
        self.cloud.delete_local_render('gem', 'gem_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'gem.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("gem", "gem_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "gem" + '\\' + "gem_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "gem" + '\\' + "gem_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "宝石材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("gem" ,difference))
        assert difference < 100

    @allure.story('玻璃gpu和老版本对比')
    def test_cloud_render_glass(self):
        self.cloud.delete_local_render('glass', 'glass_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glass.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("glass", "glass_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "glass" + '\\' + "glass_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "glass" + '\\' + "glass_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "玻璃材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("glass" ,difference))
        assert difference < 100

    @allure.story('闪粉gpu和老版本对比')
    def test_cloud_render_glitter(self):
        self.cloud.delete_local_render('glitter', 'glitter_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glitter.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("glitter", "glitter_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "glitter" + '\\' + "glitter_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "glitter" + '\\' + "glitter_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "闪粉材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("glitter" ,difference))
        assert difference < 100

    @allure.story('次表面散射gpu和老版本对比')
    def test_cloud_render_subsurface_scattering(self):
        self.cloud.delete_local_render('subsurface_scattering', 'subsurface_scattering_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'subsurface_scattering.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("subsurface_scattering", "subsurface_scattering_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "subsurface_scattering" + '\\' + "subsurface_scattering_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "subsurface_scattering" + '\\' + "subsurface_scattering_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "次表面散射材质", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("subsurface_scattering" ,difference))
        assert difference < 100

    @allure.story('地面阴影及灯光跟随gpu和老版本对比')
    def test_cloud_render_shadow_locking(self):
        self.cloud.delete_local_render('shadow_locking', 'shadow_locking_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'shadow_locking.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("shadow_locking", "shadow_locking_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "shadow_locking" + '\\' + "shadow_locking_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "shadow_locking" + '\\' + "shadow_locking_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "地面阴影及灯光跟随", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("shadow_locking" ,difference))
        assert difference < 100

    @allure.story('面光源球形灯等gpu和老版本对比')
    def test_cloud_render_all_light(self):
        self.cloud.delete_local_render('all_light', 'all_light_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'all_light.sproj')
        self.cloud.open_render_sproj('press')
        self.cloud.video_propetry_scroll_big()
        file_path = self.cloud.choose_render_filepath("all_light", "all_light_gpu", 'gpu', "off")
        self.cloud.assert_render_picture(file_path)
        matte_picture = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "all_light" + '\\' + "all_light_gpu" + '.png'
        matte_picture_old = os.path.join(OperationFile().get_garder_path('studio'), 'resolution', 'picture_diff_1920', 'CloudRender') + '\\' + "all_light" + '\\' + "all_light_gpu_old" + '.png'
        self.cloud.show_allure_picture(matte_picture, matte_picture_old, "面光源球形灯等", "本地gpu渲染照片", "本地gpu渲染老照片")
        difference = OperationFile().contrast_image(matte_picture, matte_picture_old)
        self.log.info("%s 软件离线渲染gpu新老照片比较差别:%s" % ("all_light" ,difference))
        assert difference < 100