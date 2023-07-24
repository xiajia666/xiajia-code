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
@allure.feature('本地渲染GPU和CPU对比')
@allure.severity(allure.severity_level.BLOCKER)
class TestRenderCpuGpuDiff:

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

    @allure.story('消光cpu 和 gpu 渲染对比')
    def test_cloud_render_matte(self):
        self.cloud.delete_local_render('matte', 'matte_cpu')
        self.cloud.delete_local_render('matte', 'matte_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'matte.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'matte', 'matte_cpu', 'matte_gpu', '消光材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('丝绸cpu 和 gpu 渲染对比')
    def test_cloud_render_silk(self):
        self.cloud.delete_local_render('silk', 'silk_cpu')
        self.cloud.delete_local_render('silk', 'silk_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'silk.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'silk', 'silk_cpu', 'silk_gpu','丝绸材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('反光cpu 和 gpu 渲染对比')
    def test_cloud_render_shiny(self):
        self.cloud.delete_local_render('shiny', 'shiny_cpu')
        self.cloud.delete_local_render('shiny', 'shiny_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'shiny.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'shiny', 'shiny_cpu', 'shiny_gpu','反光材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('绒cpu 和 gpu 渲染对比')
    def test_cloud_render_velvet(self):
        self.cloud.delete_local_render('velvet', 'velvet_cpu')
        self.cloud.delete_local_render('velvet', 'svelvet_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'velvet.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'velvet', 'velvet_cpu', 'velvet_gpu','绒材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('皮革cpu 和 gpu 渲染对比')
    def test_cloud_render_leather(self):
        self.cloud.delete_local_render('leather', 'leather_cpu')
        self.cloud.delete_local_render('leather', 'leather_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'leather.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'leather', 'leather_cpu', 'leather_gpu','皮革材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('金属cpu 和 gpu 渲染对比')
    def test_cloud_render_metal(self):
        self.cloud.delete_local_render('metal', 'metal_cpu')
        self.cloud.delete_local_render('metal', 'metal_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'metal.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'metal', 'metal_cpu', 'metal_gpu','金属材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('塑料cpu 和 gpu 渲染对比')
    def test_cloud_render_plastic(self):
        self.cloud.delete_local_render('plastic', 'plastic_cpu')
        self.cloud.delete_local_render('plastic', 'plastic_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'plastic.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'plastic', 'plastic_cpu', 'plastic_gpu','塑料材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('镭射cpu 和 gpu 渲染对比')
    def test_cloud_render_laser(self):
        self.cloud.delete_local_render('laser', 'laser_cpu')
        self.cloud.delete_local_render('laser', 'laser_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'laser.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'laser', 'laser_cpu', 'laser_gpu','镭射材质', 'cpu图片', 'gpu图片', 'off')

    @pytest.mark.skip
    @allure.story('毛皮cpu 和 gpu 渲染对比')
    def test_cloud_render_fur(self):
        self.cloud.delete_local_render('fur', 'fur_cpu')
        self.cloud.delete_local_render('fur', 'fur_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'fur.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'fur', 'fur_cpu', 'fur_gpu','毛皮材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('自发光cpu 和 gpu 渲染对比')
    def test_cloud_render_light(self):
        self.cloud.delete_local_render('light', 'light_cpu')
        self.cloud.delete_local_render('light', 'light_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'light.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'light', 'light_cpu', 'light_gpu','自发光材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('宝石cpu 和 gpu 渲染对比')
    def test_cloud_render_gem(self):
        self.cloud.delete_local_render('gem', 'gem_cpu')
        self.cloud.delete_local_render('gem', 'gem_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'gem.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'gem', 'gem_cpu', 'gem_gpu','宝石材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('玻璃cpu 和 gpu 渲染对比')
    def test_cloud_render_glass(self):
        self.cloud.delete_local_render('glass', 'glass_cpu')
        self.cloud.delete_local_render('glass', 'glass_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glass.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'glass', 'glass_cpu', 'glass_gpu','玻璃材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('闪粉cpu 和 gpu 渲染对比')
    def test_cloud_render_glitter(self):
        self.cloud.delete_local_render('glitter', 'glitter_cpu')
        self.cloud.delete_local_render('glitter', 'glitter_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'glitter.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'glitter', 'glitter_cpu', 'glitter_gpu','闪粉材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('次表面散射cpu 和 gpu 渲染对比')
    def test_cloud_render_subsurface_scattering(self):
        self.cloud.delete_local_render('subsurface_scattering', 'subsurface_scattering_cpu')
        self.cloud.delete_local_render('subsurface_scattering', 'subsurface_scattering_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'subsurface_scattering.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'subsurface_scattering', 'subsurface_scattering_cpu', 'subsurface_scattering_gpu','次表面散射材质', 'cpu图片', 'gpu图片', 'off')

    @allure.story('地面阴影及灯光跟随cpu 和 gpu 渲染对比')
    def test_cloud_render_shadow_locking(self):
        self.cloud.delete_local_render('shadow_locking', 'shadow_locking_cpu')
        self.cloud.delete_local_render('shadow_locking', 'shadow_locking_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_right')
        self.style.add_open_sproj('sproj', 'shadow_locking.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'shadow_locking', 'shadow_locking_cpu', 'shadow_locking_gpu','地面阴影及灯光跟随', 'cpu图片', 'gpu图片', 'off')

    @allure.story('面光源球形灯等cpu 和 gpu 渲染对比')
    def test_cloud_render_all_light(self):
        self.cloud.delete_local_render('all_light', 'all_light_cpu')
        self.cloud.delete_local_render('all_light', 'all_light_gpu')
        self.operationfile.snapshotdialogImage_change('snapshotDialogImage_front')
        self.style.add_open_sproj('sproj', 'all_light.sproj')
        self.cloud.render_cpu_gpu_diff('不切视角', 'all_light', 'all_light_cpu', 'all_light_gpu','面光源球形灯等', 'cpu图片', 'gpu图片', 'off')
