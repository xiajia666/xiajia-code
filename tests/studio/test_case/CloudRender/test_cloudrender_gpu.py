import os,sys
import yaml
sys.path.append('../../../../all')
import allure
from common.studio_auto import Style3DAuto
from common.operation_file import OperationFile
from common.studio_cloud import Style3DCloud
from common.logs import Log
import pytest
#云渲染查看, 云渲染不支持gpu,跳过

@pytest.mark.skip
@allure.feature('云渲染所有素材')
@allure.severity(allure.severity_level.BLOCKER)
class TestCloudRenderGpu:
    """云渲染和本地渲染对比"""

    def setup_method(self):
        self.style = Style3DAuto()
        self.log = Log()
        self.operationfile = OperationFile()
        self.cloud = Style3DCloud()
        self.log.info("测试开始")
        self.operationfile.keep_window()
        self.style.start_style3D()

    def teardown_method(self):
        self.log.info("测试结束")
        self.style.close_style3D()
        self.cloud.delete_cloudrender()
        self.cloud.delete_cloud_sproj("cloud")
        
    @allure.story('消光云渲染和离线渲染对比')
    def test_cloud_render_matte(self):
        self.cloud.delete_local_render('matte', 'matte_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'matte.sproj')
        self.cloud.cloud_render_type('matte_gpu_local', 'matte_gpu_old', 50, '消光材质', 'matte', 'matte_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('丝绸云渲染和离线渲染对比')
    def test_cloud_render_silk(self):
        self.cloud.delete_local_render('silk', 'silk_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'silk.sproj')
        self.cloud.cloud_render_type('silk_gpu_local', 'silk_gpu_old', 50, '丝绸材质', 'silk', 'silk_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('反光云渲染和离线渲染对比')
    def test_cloud_render_shiny(self):
        self.cloud.delete_local_render('shiny', 'shiny_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'shiny.sproj')
        self.cloud.cloud_render_type('shiny_gpu_local', 'shiny_gpu_old', 50, '反光材质', 'shiny', 'shiny_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('绒云渲染和离线渲染对比')
    def test_cloud_render_velvet(self):
        self.cloud.delete_local_render('velvet', 'velvet_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'velvet.sproj')
        self.cloud.cloud_render_type('velvet_gpu_local', 'velvet_gpu_old', 50, '绒材质', 'velvet', 'velvet_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('皮革云渲染和离线渲染对比')
    def test_cloud_render_leather(self):
        self.cloud.delete_local_render('leather', 'leather_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'leather.sproj')
        self.cloud.cloud_render_type('leather_gpu_local', 'leather_gpu_old', 50, '皮革材质', 'leather', 'leather_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('金属云渲染和离线渲染对比')
    def test_cloud_render_metal(self):
        self.cloud.delete_local_render('metal', 'metal_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'metal.sproj')
        self.cloud.cloud_render_type('metal_gpu_local', 'metal_gpu_old', 50, '金属材质', 'metal', 'metal_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('塑料云渲染和离线渲染对比')
    def test_cloud_render_plastic(self):
        self.cloud.delete_local_render('plastic', 'plastic_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'plastic.sproj')
        self.cloud.cloud_render_type('plastic_gpu_local', 'plastic_gpu_old', 50, '塑料材质', 'plastic', 'plastic_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('镭射云渲染和离线渲染对比')
    def test_cloud_render_laser(self):
        self.cloud.delete_local_render('laser', 'laser_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'laser.sproj')
        self.cloud.cloud_render_type('laser_gpu_local', 'laser_gpu_old', 50, '镭射材质', 'laser', 'laser_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('毛皮云渲染和离线渲染对比')
    def test_cloud_render_fur(self):
        self.cloud.delete_local_render('fur', 'fur_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'fur.sproj')
        self.cloud.cloud_render_type('fur_gpu_local', 'fur_gpu_old', 50, '毛皮材质', 'fur', 'fur_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('自发光云渲染和离线渲染对比')
    def test_cloud_render_light(self):
        self.cloud.delete_local_render('light', 'light_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'light.sproj')
        self.cloud.cloud_render_type('light_gpu_local', 'light_gpu_old', 50, '自发光材质', 'light', 'light_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('宝石云渲染和离线渲染对比')
    def test_cloud_render_gem(self):
        self.cloud.delete_local_render('gem', 'gem_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'gem.sproj')
        self.cloud.cloud_render_type('gem_gpu_local', 'gem_gpu_old', 50, '宝石材质', 'gem', 'gem_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('玻璃云渲染和离线渲染对比')
    def test_cloud_render_glass(self):
        self.cloud.delete_local_render('glass', 'glass_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glass.sproj')
        self.cloud.cloud_render_type('glass_gpu_local', 'glass_gpu_old', 50, '玻璃材质', 'glass', 'glass_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('闪粉云渲染和离线渲染对比')
    def test_cloud_render_glitter(self):
        self.cloud.delete_local_render('glitter', 'glitter_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glitter.sproj')
        self.cloud.cloud_render_type('glitter_gpu_local', 'glitter_gpu_old', 50, '闪粉材质', 'glitter', 'glitter_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('次表面散射云渲染和离线渲染对比')
    def test_cloud_render_subsurface_scattering(self):
        self.cloud.delete_local_render('subsurface_scattering', 'subsurface_scattering_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'subsurface_scattering.sproj')
        self.cloud.cloud_render_type('subsurface_scattering_gpu_local', 'subsurface_scattering_gpu_old', 50, '次表面散射材质', 'subsurface_scattering', 'subsurface_scattering_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('地面阴影及灯光跟随云渲染和离线渲染对比')
    def test_cloud_render_shadow_locking(self):
        self.cloud.delete_local_render('shadow_locking', 'shadow_locking_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_right')
        self.style.add_open_sproj('sproj', 'shadow_locking.sproj')
        self.cloud.cloud_render_type('shadow_locking_gpu_local', 'shadow_locking_gpu_old', 50, '地面阴影及灯光跟随', 'shadow_locking', 'shadow_locking_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')

    @allure.story('面光源球形灯等云渲染和离线渲染对比')
    def test_cloud_render_all_light(self):
        self.cloud.delete_local_render('all_light', 'all_light_gpu_local')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'all_light.sproj')
        self.cloud.cloud_render_type('all_light_gpu_local', 'all_light_gpu_old', 50, '面光源球形灯等', 'all_light', 'all_light_clo', '不切视角', 'gpu', '云渲染', '本地gpu渲染', 'on', 'png', 'clo_no_picture')



