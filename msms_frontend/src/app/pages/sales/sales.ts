import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SalesService, Sale } from '../../services/sales';

@Component({
  selector: 'app-sales',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './sales.html',
  styleUrls: ['./sales.css']
})

export class Sales implements OnInit {
  sales: Sale[] = [];
  showModal = false;
  newSale: Sale = {
    item_id: 1,
    quantity: 1,
    sale_price: 0,
    profit: 0,
    payment_method: 'Cash',
    sale_date: new Date().toISOString().slice(0, 10)
  };

  constructor(private salesService: SalesService) {}

  ngOnInit() {
    this.loadSales();
  }

  loadSales() {
    this.salesService.getSales().subscribe(data => {
      this.sales = data;
    });
  }

  openModal() {
    this.showModal = true;
  }

  closeModal() {
    this.showModal = false;
  }

  saveSale() {
    this.salesService.addSale(this.newSale).subscribe(() => {
      this.loadSales();
      this.closeModal();
    });
  }

  deleteSale(id?: number) {
    if (id) {
      this.salesService.deleteSale(id).subscribe(() => this.loadSales());
    }
  }
}


