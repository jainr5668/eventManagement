import { ElementModel } from '@patterns/element';

export class ContentModel {
  id: string;
  title: string;
  description: string[];
  event: any;
  elements: ElementModel[];
  cols: number;

  setContentValues(
    id: string,
    title?: string,
    description?: string[],
    event?: any
  ) {
    this.id = id;
    this.title = title;
    this.event = event ?? null;
    this.description = description ?? null;
  }
}
