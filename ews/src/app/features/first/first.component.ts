import { Component } from '@angular/core';
import { CardModel } from '@patterns/card';
import { FooterModel, FooterTypeEnum } from '@patterns/footer';
import { StringIds } from 'src/stringIds';

@Component({
  selector: 'feature-first',
  templateUrl: './first.component.html',
//   styleUrls: ['./app.component.css'],
})
export class FirstComponent {
  footer:FooterModel;
  card:CardModel
  constructor(){
    this.footer = new FooterModel(FooterTypeEnum.YES_NO,'footer');
    this.card = new CardModel();
    this.card.setCardValues(StringIds.cFIRSTNAME,()=>{},'cdcdcd',this.footer)
  }
}
