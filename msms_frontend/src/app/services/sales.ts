import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Sale {
  sale_id?: number;
  item_id: number;
  quantity: number;
  sale_price: number;
  profit: number;
  payment_method: 'Cash' | 'Card' | 'Online';
  sale_date: string;
}

@Injectable({ providedIn: 'root' })
export class SalesService {
  private apiUrl = 'http://127.0.0.1:5000/api/sales';

  http = inject(HttpClient);

  getSales(): Observable<Sale[]> {
    return this.http.get<Sale[]>(`${this.apiUrl}/`);
  }

  addSale(sale: Sale): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, sale);
  }

  updateSale(id: number, sale: Sale): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, sale);
  }

  deleteSale(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
