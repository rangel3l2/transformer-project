export interface Parameter {
    color: string;
    dielectric_loss_factors100g: number;
    dielectric_loss_factors25g: number;
    dielectric_loss_factors90g: number;
    dielectric_rigidity: number;
    energized: string;
    id_parameter: number;
    indice_neutralization: number;
    interfacial_tension: number;
    num_sample: number;
    oil_type: string;
    param_color: string;
    reason_analisys: string;
    registry: string | null;
    relative_umidity: number;
    sampler: string;
    sampling_point: string;
    temp_env: number;
    temp_equip: number;
    temp_sample: number;
    visual_aspect: string;
    water_content: number;
  }