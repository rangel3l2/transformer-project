import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { AnalysisData } from '../models/AnalysisData';

@Injectable({
  providedIn: 'root',
})
export class AnalysisService {
  baseUrl = 'http://192.168.1.105:5000/api/analisys';
  constructor(private http: HttpClient) {}
  getAnalysis(): Observable<AnalysisData[]> {
    return this.http
      .get<AnalysisData[]>(this.baseUrl, {
        headers: new HttpHeaders({
          'Content-Type': 'application/json',
        }),
      })
      .pipe(catchError(this.handleError));
  }
  private handleError(errorResponse: HttpErrorResponse) {
    if (errorResponse.error instanceof ErrorEvent) {
      console.error('Client Side Error :', errorResponse.error.message);
    } else {
      console.error('Server Side Error :', errorResponse);
    }
    return throwError(
      () =>
        'There is a problem with the service. We are notified & working on it. Please try again later.'
    );
  }
}
