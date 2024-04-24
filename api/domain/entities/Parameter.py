from infrasctructure.database.models import Parameter
class Parameter(Parameter):
    def __init__ (self, id_parameter, num_sample, sampler, energized, oil_type, temp_sample, temp_equip, temp_env, relative_umidity, sampling_point, reason_analisys, dielectric_loss_factors100g, dielectric_loss_factors25g, dielectric_loss_factors90g, dieletric_rigicity, water_content, interfacial_tension, color, param_color, visual_aspect ):
        self.id_parameter = id_parameter
        self.num_sample = num_sample
        self.sampler = sampler
        self.energized = energized
        self.oil_type = oil_type
        self.temp_sample = temp_sample
        self.temp_equip = temp_equip
        self.temp_env = temp_env
        self.relative_umidity = relative_umidity
        self.sampling_point = sampling_point
        self.reason_analisys = reason_analisys
        self.dielectric_loss_factors100g = dielectric_loss_factors100g
        self.dielectric_loss_factors25g = dielectric_loss_factors25g
        self.dielectric_loss_factors90g = dielectric_loss_factors90g
        self.dieletric_rigicity = dieletric_rigicity
        self.water_content = water_content
        self.interfacial_tension = interfacial_tension
        self.color = color
        self.param_color = param_color
        self.visual_aspect = visual_aspect
        
        
    def __dict__(self):
        return {'id_parameter': self.id_parameter, 'num_sample': self.num_sample, 'sampler': self.sampler, 'energized': self.energized, 'oil_type': self.oil_type, 'temp_sample': self.temp_sample, 'temp_equip': self.temp_equip, 'temp_env': self.temp_env, 'relative_umidity': self.relative_umidity, 'sampling_point': self.sampling_point, 'reason_analisys': self.reason_analisys, 'dielectric_loss_factors100g': self.dielectric_loss_factors100g, 'dielectric_loss_factors25g': self.dielectric_loss_factors25g, 'dielectric_loss_factors90g': self.dielectric_loss_factors90g, 'dieletric_rigicity': self.dieletric_rigicity, 'water_content': self.water_content, 'interfacial_tension': self.interfacial_tension, 'color': self.color, 'param_color': self.param_color, 'visual_aspect': self.visual_aspect}