import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse, } from '@angular/common/http';
import { Transformer } from '../models/Transformer';
import { Observable, catchError, throwError } from 'rxjs';
Observable
@Injectable({
  providedIn: 'root'
})
export class EquipmentService {
  baseUrl = 'http://192.168.1.105:5000/api/equipment'
  constructor(private http: HttpClient) {}
  getEquipment(): Observable<Transformer[]> {
    return this.http.get<Transformer[]>(this.baseUrl,{
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
      
    })
    .pipe(catchError(this.handleError));
  }
  private handleError(errorResponse: HttpErrorResponse) {
  
    if (errorResponse.error instanceof ErrorEvent) {
      console.error('Client Side Error :', errorResponse.error.message);
    } else {
      console.error('Server Side Error :', errorResponse);
    }
    return throwError(()=> 'There is a problem with the service. We are notified & working on it. Please try again later.');
  }

}
