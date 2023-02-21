import { Component, OnInit, Input, Output, EventEmitter, Injector } from "@angular/core";
import { TranslateService } from "@ngx-translate/core";
import { clickListenerEvent } from "@patterns/common.model";
import { Observable } from "rxjs";
import { StringIdsType } from "src/stringIds";
import { CardModel } from "./card.model";

@Component({
  selector: 'pattern-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
})
export class CardComponent {
  @Input() public card: CardModel;

  @Output() clickListener = new EventEmitter();

  constructor(private translate: TranslateService) {
    // translate.setDefaultLang('en');
    // translate.use('en');
  }

  public getLocalizedString$(stringId: StringIdsType): Observable<string> {
    return this.translate.stream(stringId);
  }

  onClicked(event: Event) {
    if (this.card.event) {
      this.card.event(event);
    } else {
      this.clickListener.emit(event);
    }
  }
}
