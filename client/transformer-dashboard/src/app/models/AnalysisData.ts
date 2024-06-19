import { Analysis } from './Analysis';
import { Chemical } from './Chemicals';
import { Transformer } from './Transformer';
import { Parameter } from './Parameter';

export interface AnalysisData {
    analysis: Analysis;
    chemical: Chemical;
    equipment: Transformer;
    parameter: Parameter;
  }