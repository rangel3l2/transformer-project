export interface Chemical {
    acetylene: number;
    carbon_dioxide: number;
    carbon_monoxide: number;
    co2_co_ratio?: number;
    ethane: number;
    ethylene: number;
    hidrogen: number;
    id_chemical_analized: number;
    methane: number;
    nitrogen?: number;
    oxygen?: number;
    registry?: string | null;
    total_combustible_gases?: number;
    total_gases?: number;
    status?: string
  }